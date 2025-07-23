# Probando-codex (Vite + React + TailwindCSS)

Proyecto fullstack basado en React, TypeScript, TailwindCSS y Radix UI, listo para desarrollo local y despliegue en Render.com.

---

## 🚀 Desarrollo local

1. Instala dependencias:
   ```bash
   npm install
   ```
2. Corre el servidor local:
   ```bash
   npm run dev
   ```
3. Abre [http://localhost:8080](http://localhost:8080) en tu navegador.

---

## 🛠️ Scripts útiles
- `npm run dev`: Servidor de desarrollo
- `npm run build`: Compila la app para producción
- `npm run preview`: Previsualiza la build localmente
- `npm run lint`: Linter de código

---

## 🌐 Deploy en Render.com

> **Nota:** El script `start` en `package.json` está configurado así:
> ```json
> "start": "vite preview --port ${PORT:-8000}"
> ```
> Esto permite que Render.com use el puerto que requiere (por la variable de entorno `$PORT`), pero en local puedes correr `npm run start` y abrir [http://localhost:8000](http://localhost:8000) si lo deseas. El comando `npm run dev` sigue usando el puerto 8080 por defecto para desarrollo rápido.


> **Nota:** El archivo `package.json` incluye el script:
> ```json
> "start": "vite preview"
> ```
> Esto es requerido por Render.com para levantar la aplicación después de la build. No afecta el diseño ni el funcionamiento local.

1. **Build Command**:  
   ```bash
   npm run build
   ```
2. **Start Command**:  
   ```bash
   npm run preview
   ```
3. **Configuración de puertos**: Render detecta automáticamente el puerto 8080.
4. **Configuración especial**: La configuración de `vite.config.ts` incluye la sección `preview` y `allowedHosts` para compatibilidad con Render.com.

---

## 📝 Notas
- Si modificas la configuración de Tailwind, Vite o PostCSS, asegúrate de reiniciar el servidor local.
- El diseño y los estilos están alineados con el proyecto original. Si el diseño se rompe tras un cambio, revisa los archivos de configuración y dependencias.

---

**¡Listo para desarrollar y desplegar!**
React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.
