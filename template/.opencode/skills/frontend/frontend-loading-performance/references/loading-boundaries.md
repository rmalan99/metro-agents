# Fronteras de carga

Cada frontera observable define:

- región y disparador;
- tamaño estable o skeleton representativo;
- texto/estado accesible y `aria-busy` cuando aplique;
- error contextual y reintento real;
- comportamiento de foco al aparecer contenido;
- test IDs estables para región, loading y error cuando sean necesarios.

No sustituyas toda la página si solo carga una región. No dejes controles activables antes de que su dependencia exista. Un fallback breve evita parpadeo innecesario; uno prolongado comunica qué se espera. Verifica éxito, fallo y navegación rápida con Playwright sin crear tests persistentes salvo solicitud explícita.
