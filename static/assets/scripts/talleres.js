$(() => {
  let converter = new showdown.Converter();
  $(".taller-descripcion").toArray().forEach((e, i) => {
    let raw = $(e).text();
    $(e).html(converter.makeHtml(raw));
  });

  $(".disertante-about").toArray().forEach((e, i) => {
    let raw = $(e).text();
    $(e).html(converter.makeHtml(raw));
  });

  $(".taller-temario").toArray().forEach((e, i) => {
    let raw = $(e).text();
    $(e).html(converter.makeHtml(raw));
  });
});
