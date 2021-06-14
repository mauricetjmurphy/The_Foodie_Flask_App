$(document).ready(function () {
    $(".alert").delay(3000).slideUp(400);
});

$(document).ready(function () {
    var max_input_fields = 10;
    var add_input = $(".add-ingredient");
    var input_wrapper = $(".ingredients");
    var add_input_count = 1;
    var new_input = `<input
    value=""
    type="text"
    name="ingredient-field[]"
    class="ingredient_input"
    placeholder="Ingredient *"
    required
/>`;
    $(add_input).click(function () {
        if (add_input_count < max_input_fields) {
            add_input_count++;
            $(input_wrapper).append(new_input);
        }
    });
});

$(document).ready(function () {
    var add_input = $(".remove-ingredient");
    var input_wrapper = $(".ingredients");
    $(add_input).click(function () {
        $(input_wrapper).children().last().remove();
    });
});

$(document).ready(function () {
    var max_input_fields = 10;
    var add_input = $(".add-step");
    var input_wrapper = $(".steps");
    var add_input_count = 1;
    var new_input = `<textarea
    rows="3"
    value=""
    type="text"
    name="step-field[]"
    class="step_input"
    placeholder="Step *"
    required
></textarea>`;
    $(add_input).click(function () {
        if (add_input_count < max_input_fields) {
            add_input_count++;
            $(input_wrapper).append(new_input);
        }
    });
});

$(document).ready(function () {
    var add_input = $(".remove-step");
    var input_wrapper = $(".steps");
    $(add_input).click(function () {
        $(input_wrapper).children().last().remove();
    });
});
