<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>

$(document).ready(function(){
    $("#id_parent_category").change(function(){
    parent_category = $(this).val();
    // elementImage = document.getElementsByClassName("form-row field-image");
    if (parent_category == 0) 
        $('#id_image').show()
     else 
        $('#id_image').hide()
    });
});