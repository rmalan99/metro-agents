# Pipeline normativo de entrega Supabase

## Modelo de jobs

```text
validate-config
  └─ quality
      ├─ web-tests
      ├─ api-tests
      └─ migration-test-ephemeral
           └─ build-artifacts
                └─ migration-plan
                     └─ migrate-once
                          ├─ configure-runtime
                          └─ deploy-functions
                               └─ deploy-web
                                    └─ smoke-tests
```

Agrupa jobs solo si conserva fallos claros y no reduce seguridad. Separa Web/API aunque compartan el mismo workflow.

## CI de pull request

1. Checkout con permisos de solo lectura.
2. Validación de archivos y nombres de variables, nunca valores secretos.
3. Instalación reproducible con lockfile.
4. Formato, lint, typecheck y pruebas por ámbito.
5. Construcción del artefacto Web sin credenciales privilegiadas.
6. Aplicación completa de migraciones en base efímera.
7. Pruebas SQL/RLS, funciones y compatibilidad de tipos.
8. Preview opcional con datos sintéticos y expiración automática.

Un fork no recibe secretos. Los pasos que los necesitan no se ejecutan con código no confiable.

## CD protegido

1. Usa el commit exacto validado; no reconstruyas desde una rama mutable si puede promoverse el artefacto.
2. Adquiere exclusión mutua por entorno. No canceles una migración ya iniciada.
3. Verifica destino, versión de CLI, identidad y variables obligatorias.
4. Genera plan/dry run de migraciones y falla ante divergencia.
5. Solicita aprobación cuando el riesgo o entorno lo requiera.
6. Aplica migraciones una sola vez desde un único job.
7. Configura secretos del runtime sin imprimirlos.
8. Despliega Edge Functions declaradas y verifica versión/configuración.
9. Despliega Web con URL y publishable key del mismo entorno.
10. Ejecuta smoke tests y registra commit, migraciones y artefactos.

## Variables y secretos

| Clase        | Ejemplos                                 | Destino permitido                                          |
| ------------ | ---------------------------------------- | ---------------------------------------------------------- |
| Pública      | URL, project ref, publishable key        | build Web y runtime público                                |
| Despliegue   | token scoped, credencial de hosting      | runner protegido                                           |
| Runtime      | claves de terceros, webhook/cron secrets | secretos de Edge Functions                                 |
| Privilegiada | service role, contraseña de DB           | solo servidor; evita guardarla si la plataforma la inyecta |

- Usa tokens scoped por proyecto, permiso y expiración.
- No copies secretos a variables públicas ni artefactos.
- Evita archivos temporales con secretos; si son inevitables, créalos en almacenamiento temporal con permisos restrictivos y elimínalos en un paso `always`.

## Compatibilidad y recuperación

- **Expansión:** añade objetos/campos compatibles y despliega lectores tolerantes.
- **Migración:** rellena datos de forma acotada y observable.
- **Contracción:** elimina compatibilidad antigua en una entrega posterior tras verificar consumidores.
- Un rollback Web/función no revierte automáticamente la base. Mantén el esquema compatible con la versión anterior durante la ventana definida.
- Si falla una migración, detén funciones y Web dependientes; inspecciona transacción e historial antes de reintentar.
- Si falla una función o Web después de migrar, corrige hacia delante o restaura el artefacto compatible.
- Smoke tests cubren salud, lectura pública, operación autenticada crítica y rechazo no autorizado.
