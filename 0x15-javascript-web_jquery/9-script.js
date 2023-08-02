const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.getJSON(url, function (data) {
  const hello = data.hello;
  $('DIV#hello').text(hello);
});
