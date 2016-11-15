var edit = edit || [];
edit.bindForm = function(keys) {
    console.log("hei")
    keys.forEach(function(key) {
      $('#edit-item-' + key).click(function() {
          console.log('key', key)
          $('#edit-form-' + key).show();
          $('#item-info-' + key).hide();
      });
      $('#cancel-item-' + key).click(function() {
          console.log('key', key)
          $('#edit-form-' + key).hide();
          $('#item-info-' + key).show();
      });
    });
};
