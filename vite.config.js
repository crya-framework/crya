import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";
import crya from "crya-vite-plugin";

export default defineConfig({
  plugins: [crya(), tailwindcss()],
  build: {
    manifest: true,
    outDir: "public/build",
    rollupOptions: {
      input: ["resources/js/app.js", "resources/css/app.css"],
    },
  },
});
