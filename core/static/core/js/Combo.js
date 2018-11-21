$(document).ready(function(){
    //capturamos cuando el usuario seleccione una opcion del combobox
  
    $("#cboregion").change(function(){
        // Este motodo se ejecuta cuando el usuario cambia de opcion en el combobox

        var regionid = $("#cboregion").val();

        console.log(regionid);

        //enviamos el id rescatado a un archivo php para obtener los option

        $.get("Combo.php",{id:regionid}, function(respuestacomuna){
            //recibimos la respuesta
            console.log(respuestacomuna);
            $("#cbocomuna").html(respuestacomuna);
            //habilitamos el combobox
            $("#cbocomuna").prop("disabled",false)
        });
    });
});