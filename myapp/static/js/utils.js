const eliminar = (ruta) => {
  Swal.fire({
    title: "Estas Seguro?",
    text: "Esta acción no se puede deshacer",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#d33",
    cancelButtonColor: "#3085d6",
    confirmButtonText: "Si, Eliminar",
    cancelButtonText: "No, Cancelar"
  }).then((result) => {
    if (result.isConfirmed) {
      location.href = ruta;
    }
  });

  Swal.fire({
    title: "Sweet!",
    text: "Modal with a custom image.",
    imageUrl: "https://unsplash.it/400/200",
    imageWidth: 400,
    imageHeight: 200,
    imageAlt: "Custom image"
  });
}

const botonesEliminar = document.querySelectorAll('.btn-eliminar');

botonesEliminar.forEach((boton) => {
    boton.addEventListener('click', (e) => {
        e.preventDefault();
        Swal.fire({
            title: "Eliminar Registro",
            text: "Esta acción no se puede deshacer",
            imageUrl: "/static/img/Papelera.png",
            imageWidth: 400,
            imageHeight: 200,
            showCancelButton: true,
            confirmButtonColor: "#d33",
            cancelButtonColor: "#3085d6",
            confirmButtonText: "Eliminar"
        }).then((result) => {
            if (result.isConfirmed) {
                location.href = boton.href;
            }
        });
    });
});

