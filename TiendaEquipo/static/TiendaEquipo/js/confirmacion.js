function confirmarEliminacion(id) {
    swal({
        title: "¿Está Seguro?",
        text: "No podrá deshacer esta acción",
        icon: "warning",
        buttons: true,
        dangerMode: true,
        buttons: ["Cancelar", "Confirmar"],
      })
      .then((willDelete) => {
        if (willDelete) {
          window.location = "/eliminar-cliente/"+id+"/";
        } else {
          swal("No se Eliminó");
        }
      });
}