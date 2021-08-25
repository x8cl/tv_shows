$(document).ready(function(){
    
    /* modal */
    $('.modal-borrar').on('click', function(){
        const href= $(this).attr('data-href');
        $('#confirmar-borrar').attr('href', href);
    });

});