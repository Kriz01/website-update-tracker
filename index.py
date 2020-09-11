
def create_html_file():
    html_str =  """<html>
    <head>
    <title>Website Update Tracker</title>

    <style>
    body, html {
    height: 100%;
    margin: 0;
    }

    .bg {
    background-image: url("bg_1.jpg");
    height: 100%; 
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    }
    .layer {
        background-color: rgba(248, 247, 216, 0.7);
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    </style>
    </head>
    <body>
    """
    Html_file= open("index.html","w")
    Html_file.write(html_str)
    Html_file.close()
