const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
   devServer: {
	allowedHosts: "all",
  },
  transpileDependencies: true
})
// module.exports = {
//   devServer: {
//         // proxy : 'http://localhost:8000'
//         proxy : 'https://j7b302.p.ssafy.io/api/'
//       }
// }