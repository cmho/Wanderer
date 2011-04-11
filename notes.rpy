init python:

    # Message Styles

    style.messageWindow = Style(style.window)
    style.messageColumns = Style(style.hbox)
    style.messageListBox = Style(style.vbox)
    style.messageListViewport = Style(style.viewport)
    style.messageButton = Style(style.button)
    style.messageButtonText = Style(style.button_text)
    style.messageScrollBar = Style(style.vscrollbar)
    style.messageBodyScrollBar = Style(style.vscrollbar)
    style.messageBodyBox = Style(style.vbox)
    style.messageBodyViewport = Style(style.viewport)
    style.messageText = Style(style.say_dialogue)
    style.messageControls = Style(style.hbox)

    # Default style values...

    style.messageWindow.ymaximum = 600

    style.messageColumns.spacing = 10

    style.messageListViewport.xminimum = 280
    style.messageListViewport.xmaximum = 280

    style.messageListBox.yalign = 0.0

    style.messageButton["Message"].xfill = True
    style.messageButton["CurrentMessage"].xfill = True

    style.messageButtonText["Message"].color="#99A"
    style.messageButtonText["CurrentMessage"].color="#FFF"

    style.messageBodyViewport.xminimum = 460
    style.messageBodyViewport.xmaximum = 460
    style.messageBodyViewport.ymaximum = 550

    style.messageBodyScrollBar.ymaximum=550

    style.messageControls.spacing = 10

    def init_messages():
        if hasattr(store, "messages") == False:
            store.messages = []

    def add_message(subject, sender, message, condition=None):
        init_messages()
        store.messages.append( (subject, sender, message, condition) )

    def show_messages():
        message = None

        while message != -1:
            message = show_message_ui(message)

    def show_message_ui(currentMessage):

        init_messages()

        messageCount = count_messages()

        ui.window(style=style.messageWindow)
        ui.hbox(style=style.messageColumns) # For the three columns of controls

        vp = ui.viewport(style=style.messageListViewport)

        ui.window(style=style.messageListBox)
        ui.vbox() # For the mail list

        index = 0
        for message in store.messages:
            if (message[3] == None or eval(message[3]) == True):
                    styleIndex = "Message"
                    if (index == currentMessage):
                        styleIndex = "CurrentMessage"
                    ui.button(clicked=ui.returns(index),
                        style=style.messageButton[styleIndex])
                    ui.text(message[0] + " - " + message[1], style=style.messageButtonText[styleIndex])
            index = index + 1

        ui.close() # mail list vbox

        ui.bar(adjustment=vp.yadjustment, style=style.messageScrollBar)

        ui.window(style=style.messageBodyBox)
        ui.vbox() # For the right-hand stuff; message and buttons

        ui.hbox()
        vp2 = ui.viewport(style=style.messageBodyViewport)

        if (currentMessage >= 0) and (currentMessage < messageCount):
            hasMessage = True
            ui.text(store.messages[currentMessage][2], style=style.messageText)
        else:
            hasMessage = False
            ui.null()
        ui.bar(adjustment=vp2.yadjustment, style=style.messageBodyScrollBar)

        ui.close()

        ui.hbox(style=style.messageControls) # For the buttons

        ui.button(clicked=ui.returns(-1),
            style=style.messageButton["Close Messages"])
        ui.text("Close Messages", style = style.messageButtonText["Close Messages"])
        if hasMessage:
            ui.button(clicked=ui.returns(-2),
                style=style.messageButton["Delete Message"])
            t = ui.text("Delete Message", style = style.messageButtonText["Delete Message"])

        ui.close() # buttons hbox


        ui.close() # right-hand column vbox
        ui.close() # columns hbox

        result = ui.interact()

        if result == -2: #(delete current message)
            del store.messages[currentMessage]
            return None
        else:
            return result

    def count_messages():
        init_messages()
        return len(store.messages)

    def count_visible_messages():
        init_messages()

        count = 0

        for message in store.messages:
            if (message[3] == None or eval(message[3]) == True):
                count = count + 1
        return count