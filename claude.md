# Panel de Rossvtienda (`panel.rossvtienda.com`)

App de administración de **Rossvtienda** (flores eternas de listón satinado y ramos con carritos Hot
Wheels, León, Guanajuato). La usa **la dueña, casi siempre desde el celular**, sin conocimientos
técnicos. Tiene dos áreas con **un solo inicio de sesión**:

1. **Catálogo:** productos, secciones, fotos, colores y Papelera. Es lo que hoy está en
   `https://rossvtienda.com/admin/` y se va a mudar aquí.
2. **Inventario y ventas (nuevo):** materiales, compras, ventas y ganancias, para saber cuánto
   cuesta hacer cada producto, cuánto se gana y cuánto se gasta.

**Estado:** por empezar. Esta carpeta solo tiene este archivo.

## Contexto: esta carpeta vive dentro del repositorio del sitio

El repositorio es `SuprSalva/RosasViri`. La raíz (`..`) es el **sitio público** en Astro, publicado
en `https://rossvtienda.com`. Antes de cambiar algo grande, lee:

- `../README.md`: cómo funciona el sitio, el panel actual, Supabase y Cloudflare.
- `../PLAN_DE_TRABAJO.md`: decisiones del proyecto y su historia.
- `../docs/auditoria-seguridad.md`: hallazgos de seguridad y cómo se resolvieron.

| Pieza | Dónde | Notas |
|---|---|---|
| Panel actual (para migrar) | `../src/pages/admin.astro`, `../src/lib/panel/` (`app.ts`, `dom.ts`, `fotos.ts`) | Sigue en producción hasta la mudanza: **no romperlo** |
| Base de datos (Supabase) | `../supabase/migrations/` | **La misma** para el sitio y el panel |
| Servicio que sube fotos y publica el sitio | `../supabase/functions/panel/` | Lo llama el panel con `accion: 'subir-foto'` y `accion: 'publicar'` |
| Publicación del sitio | `../.github/workflows/publicar.yml` | Cloudflare Pages, proyecto `rossvtienda` |
| Colores y tipografías de la marca | `../src/styles/global.css` | Copiar las variables, no inventar otras |

Si Claude Code se abre en `panel/`, los cambios fuera de esta carpeta (`../supabase`, `../.github`,
`../public`) piden permiso. Es normal.

## Decisiones tomadas (no volver a discutirlas)

- **Subdominio propio** `panel.rossvtienda.com`, para separar la sesión del panel de los scripts
  del sitio público (Analytics, pixeles o pagos en el futuro). El dominio ya está en Cloudflare.
- **Misma base de datos:** el mismo proyecto de Supabase. **No crear otro proyecto** ni otra carpeta
  `supabase/` aquí. Toda migración nueva va en `../supabase/migrations/`.
- **Mismo stack que el sitio:** Astro en modo estático, TypeScript y `@supabase/supabase-js`, **sin
  framework de interfaz**. El DOM se arma con el ayudante `el()` de `dom.ts`.
- **Hosting:** Cloudflare Pages (plan gratis), con un proyecto nuevo `rossvtienda-panel` y su propio
  flujo de GitHub Actions.
- **Todo en español:** nombres de variables y funciones, comentarios, textos y mensajes de commit.

## Stack y comandos

- Node 22 (usa `../.nvmrc`). Mismas versiones que la raíz: `astro` 7 y `typescript` 6
  (`@astrojs/check` todavía no acepta TypeScript 7).
- Este proyecto tiene su propio `package.json` y su propio `node_modules`.

