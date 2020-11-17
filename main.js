const { app, BrowserWindow } = require('electron')

function createWindow() {
    const win = new BrowserWindow ({
        width: 800,
        height: 600,
        resizable: false,
        webPreferences: {
            nodeIntegration: true
        }
    })
    win.loadFile(__dirname + '/html/dashboard.html')
}

app.whenReady().then(createWindow)

app.on('window-all-closed', ()=> {
    if(process.platform !== 'darwin') {
        app.quit()
    }
})

app.on('activate', ()=> {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow()
    }
})