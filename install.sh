#!/usr/bin/env bash

set -Eeuo pipefail

REPOSITORY="${METRO_AGENTS_REPOSITORY:-rmalan99/metro-agents}"
REF="${METRO_AGENTS_REF:-main}"
ARCHIVE_URL="https://github.com/${REPOSITORY}/archive/${REF}.tar.gz"

info() {
  printf '[metro-agents] %s\n' "$*"
}

fail() {
  printf '[metro-agents] Error: %s\n' "$*" >&2
  exit 1
}

for command in curl tar git mktemp; do
  command -v "$command" >/dev/null 2>&1 || fail "Se requiere el comando '$command'."
done

project_root="$(git rev-parse --show-toplevel 2>/dev/null)" || \
  fail "Ejecuta el instalador dentro de un repositorio Git."

temporary_directory="$(mktemp -d)"
trap 'rm -rf "$temporary_directory"' EXIT

info "Descargando ${REPOSITORY}@${REF}..."
curl -fsSL "$ARCHIVE_URL" | tar -xz -C "$temporary_directory"

source_root="$(find "$temporary_directory" -mindepth 1 -maxdepth 1 -type d -print -quit)"
package_root="${source_root}/template"

[[ -d "$package_root" ]] || fail "La versión descargada no contiene el directorio template/."

mapfile -d '' package_entries < <(find "$package_root" -mindepth 1 -maxdepth 1 -print0)
(( ${#package_entries[@]} > 0 )) || fail "El paquete template/ está vacío."

timestamp="$(date -u +'%Y%m%dT%H%M%SZ')"
backup_root="${project_root}/.metro-agents-backups/${timestamp}-$$"
backup_created=false

for source_path in "${package_entries[@]}"; do
  entry_name="$(basename "$source_path")"
  destination_path="${project_root}/${entry_name}"

  if [[ -e "$destination_path" || -L "$destination_path" ]]; then
    mkdir -p "$backup_root"
    cp -a "$destination_path" "$backup_root/"
    backup_created=true
  fi
done

cp -a "$package_root/." "$project_root/"

info "Contenido instalado en ${project_root}."
if [[ "$backup_created" == true ]]; then
  info "Respaldo creado en ${backup_root}."
else
  info "No había archivos anteriores que respaldar."
fi
info "OpenCode recargará la configuración automáticamente; también puedes usar /reload."
