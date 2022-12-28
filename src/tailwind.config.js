/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./assets/**/*.{py,html,js}",
    "./components/**/*.{py,html,js}",
    "./data/**/*.{py,html,js}",
    "./pages/**/*.{py,html,js}",
    "./utils/**/*.{py,html,js}",
    "./app.py"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography')
  ],
}
