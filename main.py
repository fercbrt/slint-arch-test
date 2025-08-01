# /opt/mi-app/mi_app.py
import slint

UI = """
export component MainWindow inherits Window {
    width: 1920px;
    height: 1080px;
    background: #2b2b2b;

    Text {
        text: "Aplicación Kiosko en Arch Linux";
        color: #ffffff;
        font-size: 40px;
        x: parent.width / 2 - self.width / 2;
        y: parent.height / 2 - self.height / 2;
    }

    TouchArea {
        width: parent.width;
        height: parent.height;
        clicked => {
            // Opcional: cerrar con toque
            app.quit();
        }
    }
}
"""

app = slint.Slint(UI)
app.run()
