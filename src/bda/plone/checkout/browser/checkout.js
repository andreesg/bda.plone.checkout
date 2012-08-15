(function($) {

    $(document).ready(function() {
        var delivery_address = $('div.delivery_address');
        var toggle = function(input) {
            if (input.attr('type') == 'hidden') {
                delivery_address.show();
                return;
            }
            if (input.attr('checked') == true) {
                delivery_address.show();
            } else {
                delivery_address.hide();
            }
        }
        var sel = 'input[name=checkout.delivery_address.alternative_delivery]';
        var input = $(sel);
        toggle(input);
        input.change(function(event) {
            toggle($(this));
        });
    });

})(jQuery);