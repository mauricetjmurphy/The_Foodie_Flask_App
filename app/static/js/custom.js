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
    class="ingredient_input mb-3"
    placeholder="Ingredient"
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
    placeholder="Step"
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

// Element selectors for the recipe form
const dishImage = document.querySelector("#dishImage");
const recipeTitle = document.querySelector("#recipeTitle");
const description = document.querySelector("#description");
const category = document.querySelector("#category");
const ingredient = document.querySelector("#ingredient");
const step = document.querySelector("#step");
const recipeForm = document.getElementById("recipeForm");

//Adding an event listener on the form submit. Conditional if/else statement validate the form
recipeForm.addEventListener("submit", (e) => {
    e.preventDefault();

    isFormValid = true;

    if (!dishImage.value) {
        const error = dishImage.parentElement.querySelector(".error-message");
        error.classList.remove("hidden");
        dishImage.classList.remove("mb-4");
        dishImage.classList.add("mb-0");
        dishImage.scrollIntoView();

        isFormValid = false;
    } else {
        const error = dishImage.parentElement.querySelector(".error-message");
        error.classList.add("hidden");
        dishImage.classList.add("mb-4");
    }
    if (!recipeTitle.value) {
        const error = recipeTitle.parentElement.querySelector(".error-message");
        error.classList.remove("hidden");
        recipeTitle.classList.remove("mb-4");
        recipeTitle.classList.add("mb-0");
        dishImage.scrollIntoView();

        isFormValid = false;
    } else {
        const error = recipeTitle.parentElement.querySelector(".error-message");
        error.classList.add("hidden");
        recipeTitle.classList.add("mb-4");
    }
    if (description.value.length < 10) {
        const error = description.parentElement.querySelector(".error-message");
        error.classList.remove("hidden");
        const min = description.parentElement.querySelector("#min-char");
        min.classList.remove("mb-4");
        min.classList.add("mb-0");
        dishImage.scrollIntoView();

        isFormValid = false;
    } else {
        const error = description.parentElement.querySelector(".error-message");
        error.classList.add("hidden");
        const min = description.parentElement.querySelector("#min-char");
        min.classList.add("mb-4");
    }
    if (category.value.length < 1) {
        const error = category.parentElement.querySelector(".error-message");
        error.classList.remove("hidden");
        category.classList.remove("mb-4");
        category.classList.add("mb-0");
        dishImage.scrollIntoView();

        isFormValid = false;
    } else {
        const error = category.parentElement.querySelector(".error-message");
        error.classList.add("hidden");
        category.classList.add("mb-4");
    }
    if (!ingredient.value) {
        const error = ingredient.parentElement.querySelector(".error-message");
        error.classList.remove("hidden");
        ingredient.classList.remove("mb-4");
        ingredient.classList.add("mb-0");
        dishImage.scrollIntoView();

        isFormValid = false;
    } else {
        const error = ingredient.parentElement.querySelector(".error-message");
        error.classList.add("hidden");
        ingredient.classList.add("mb-4");
    }
    if (!step.value) {
        const error = step.parentElement.querySelector(".error-message");
        error.classList.remove("hidden");
        step.classList.remove("mb-4");
        step.classList.add("mb-0");
        dishImage.scrollIntoView();

        isFormValid = false;
    } else {
        const error = step.parentElement.querySelector(".error-message");
        error.classList.add("hidden");
        step.classList.add("mb-4");
    }

    if (isFormValid) {
        recipeForm.submit();
    }
});
