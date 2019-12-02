

$(() => {
  $("#btn-registrar").click(() => {
    let data = getData();
    if (validar(data)) {
      HoldOn.open();
      $.ajax({
        type: 'POST',
        url: $('#url-taller').val(),
        data: data,
        success: (result) => {
          if (result.trim() == 'ok') {
            $("#title").hide();
            $("#form").hide();
            $("#message-container").show();
          } else {
            console.log("error", result);
            alert("Error inesperado al procesar la consulta");
          }
          HoldOn.close();
        }
      });
    }
  });
});


function getById(id) {
  return $(`#${id}`).val();
}




function getData() {
  return data = {
    nombre: getById('nombre'),
    apellido: getById('apellido'),
    dni: getById('dni'),
    institucion: getById('institucion'),
    profesion: getById('profesion'),
    email: getById('email'),
    telefono: getById('telefono')
  };
}


function makeAlert(field, message) {
  $(`#${field}`).notify(message, "error");
}


function checkBlanck(data, field) {
  if (data[field].trim() == '') {
    makeAlert(field, 'El campo es obligatorio')
    return false;
  } else {
    return true;
  }
}


function validar(data) {
  let result = true;
  if (data.nombre.trim() == '') {
    makeAlert('nombre', 'El campo es obligatorio')
    result = false;
  }

  if (data.apellido.trim() == '') {
    makeAlert('apellido', 'El campo es obligatorio')
    result = false;
  }

  if (data.dni.trim() == '') {
    makeAlert('dni', 'El campo es obligatorio')
    result = false;
  }

  if (isNaN(data.dni)) {
    makeAlert('dni', 'El campo no es valido')
    result = false;
  }


  if (data.institucion.trim() == '') {
    makeAlert('institucion', 'El campo es obligatorio')
    result = false;
  }

  if (data.profesion.trim() == '') {
    makeAlert('profesion', 'El campo es obligatorio')
    result = false;
  }

  if (data.email.trim() == '') {
    makeAlert('email', 'El campo es obligatorio')
    result = false;
  }
  if (data.email.trim().indexOf('@') == -1) {
    makeAlert('email', 'El campo no es valido')
    result = false;
  }

  if (data.telefono.trim() == '') {
    makeAlert('telefono', 'El campo es obligatorio')
    result = false;
  }
  return result;
}
