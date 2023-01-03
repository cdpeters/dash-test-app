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
    // extend: {
    //   backgroundImage: {
    //     image: `url('/assets/images/data_science_background.png')`,
    //   }
    // },
  },
  plugins: [
    require('@tailwindcss/typography')
  ],
}
