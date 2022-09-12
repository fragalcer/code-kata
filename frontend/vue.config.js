const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      "/backend": {
        "target": "http://0.0.0.0:8000",
        "secure": false
      },
      "/myob": {
        "target": "http://127.0.0.1:8001",
        "secure": false
      },
      "/xero": {
        "target": "http://127.0.0.1:8002",
        "secure": false
      },
      "/decisionengine": {
        "target": "http://127.0.0.1:8003",
        "secure": false
      },
    }
  }
})
