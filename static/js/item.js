var items = items || [];
items.bindForm = function(keys) {
    keys.forEach(function(key) {
      $('#bought-' + key).click(function() {
          $('#buy-item-' + key).click();
      });
    });
};
