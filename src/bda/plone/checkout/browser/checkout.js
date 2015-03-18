(function($) {

    $(document).ready(function() {
        var delivery_address = $('div.delivery_address');
        var toggle = function(input) {
            if (input.attr('type') === 'hidden') {
                delivery_address.show();
                return;
            }
            if (input.is(':checked')) {
                delivery_address.show();
            } else {
                delivery_address.hide();
            }
        };

        var fld_name = "checkout.delivery_address.alternative_delivery";
        var input = $('input[name="' + fld_name + '"]');
        toggle(input);
        input.change(function(event) {
            toggle($(this));
        });
        
        // terms and conditions overlay
        $('a.terms_and_conditions').prepOverlay({
            subtype: 'ajax',
            filter: common_content_filter,
            cssclass: 'overlay-terms-and-condition',
        });

        var payment_checked = $("input:radio[name='checkout.payment_method_selection.payment_method']:checked");
        if (payment_checked.val() != undefined) {
            if (payment_checked.val() != 'ideal') {
                $("#tag-checkout-bank_selection-heading").hide();
                $("#field-checkout-bank_selection-bank").hide();
                $("#input-checkout-bank_selection-bank-").attr('value', 'creditcard');
            }
        }

        if ($("#display-checkout-payment_method_selection-payment_method").html() == "Creditcard") {
            $("#tag-checkout-bank_selection-heading").hide();
            $("#field-checkout-bank_selection-bank").hide();
            $("#input-checkout-bank_selection-bank-").attr('value', 'creditcard');
        }

        var payment_input = $("input:radio[name='checkout.payment_method_selection.payment_method']")
        payment_input.change(function() {
            if ($(this).is(":checked")) {
                if ($(this).val() == "creditcard") {
                    $("#tag-checkout-bank_selection-heading").hide();
                    $("#field-checkout-bank_selection-bank").hide();
                    $("#input-checkout-bank_selection-bank-").attr('value','creditcard');
                } else {
                    $("#tag-checkout-bank_selection-heading").show();
                    $("#field-checkout-bank_selection-bank").show();
                    $("#input-checkout-bank_selection-bank-").attr('value','');
                }
            }
        });
        
    });

})(jQuery);
