# Autenticación y sesión

- Login, recuperación y reset usan un AuthShell coherente, separado del shell administrativo salvo requisito explícito.
- AuthShell contiene identidad real, título único, contexto breve, campos, un CTA primario y navegación secundaria.
- Login básico: identificador, contraseña, recuperación, submit y registro solo si está habilitado.
- Carga deshabilita doble envío, conserva identificador y no afirma éxito antes de respuesta autoritativa.
- Credenciales inválidas no revelan existencia de cuenta. Recuperación usa mensajes neutrales.
- Reset contempla validación pendiente, token inválido/expirado, formulario y éxito real; nunca muestra secretos ni tokens.
- MFA, SSO, captcha, invitación y registro aparecen solo con contrato real.
- Dentro del backoffice, cerrar sesión pertenece al dropdown de cuenta, limpia la sesión real y deja una salida accesible ante error.
- Móvil soporta teclado, scroll y safe areas sin alturas rígidas ni overflow horizontal.
