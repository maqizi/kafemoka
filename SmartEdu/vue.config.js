module.exports = {
    devServer: {
      proxy: {
        '/api': {
          // target: 'http://127.0.0.1:9001/api/1/', // Replace this with the base URL of your API
		  target: 'http://127.0.0.1:9001/api/1.3.0/',
          changeOrigin: true,
          ws: true,
          pathRewrite: {
            '^/api': ''
          }
        },
        
      }
    }
  }

  