module.exports = function override(config, env) {
    if (env === 'development') {
      config.watchOptions = {
        ignored: [
          '**/node_modules',
          '**/.git',
          'C:/hiberfil.sys', // تجاهل ملف النظام
        ],
      };
    }
    return config;
  };
  