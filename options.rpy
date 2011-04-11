## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python hide:

    ## Should we enable the use of developer tools? This should be
    ## set to False before the game is released, so the user can't
    ## cheat using developer tools.

    config.developer = True

    ## These control the width and height of the screen.

    config.screen_width = 800
    config.screen_height = 600

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"Wanderer"

    #########################################
    # Layouts
    
    ## This enables the use of an in-game menu that is made out of
    ## buttons.

    layout.button_menu()

    #########################################
    # Themes
    
    ## We then want to call a theme function. themes.roundrect is
    ## a theme that features the use of rounded rectangles. It's
    ## the only theme we currently support.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

    theme.diamond(
        # Color scheme: White Chocolate
                                    
        ## The color of an idle widget face.
        widget = "#33271C",

        ## The color of a focused widget face.
        widget_hover = "#ECE7C4",

        ## The color of the text in a widget.
        widget_text = "#B99D83",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#ffffff",

        ## The color of a disabled widget face. 
        disabled = "#614D3A",

        ## The color of disabled widget text.
        disabled_text = "#80654D",

        ## The color of informational labels.
        label = "#F1EBE5",

        ## The color of a frame containing widgets.
        frame = "#926841",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "#FBF9EA",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "#FBF9EA",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.            
        )


    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    style.window.background = Frame("ui/frame.png", 0, 5)

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    style.window.left_margin = 0
    style.window.right_margin = 0
    style.window.top_margin = 0
    style.window.bottom_margin = 20

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.left_padding = 20
    style.window.right_padding = 20
    style.window.top_padding = 15
    style.window.bottom_padding = 15

    ## This is the minimum height of the window, including the margins
    ## and padding.

    style.window.yminimum = 181
    
    style.say_who_window.background = Frame("ui/nametag.png", 0, 0) #Background skin
    style.say_who_window.xalign = 0.0
    style.say_who_window.yalign = 1.0
    #style.say_who_window.xpos = 100 #For precise placement
    #style.say_who_window.ypos = 100 #For precise placement
    style.say_who_window.left_margin = 0
    style.say_who_window.left_padding = 15
    style.say_who_window.top_padding = 10
    style.say_who_window.right_padding = 20
    style.say_who_window.bottom_padding = 3
    style.say_who_window.bottom_margin = 0
    style.say_who_window.xminimum = 251
    style.say_who_window.yminimum = 37
    style.say_who_window.xfill = False


    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    style.default.font = "resources/Magnificent.ttf"

    ## The default size of text.

    style.default.size = 18
    
    style.default.color = "#24221d"

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to False if the game does not have voicing.

    config.has_voice = False

    ## Sounds that are used when button and imagemaps are clicked.

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.

    # config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.

    # config.main_menu_music = "main_menu_theme.ogg"


    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.   
    config.help = "README.html"


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = None

    ## Used when exiting the game menu to the game.
    config.exit_transition = None

    ## Used between screens of the game menu.
    config.intra_transition = None

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = None

    ## Used when returning to the main menu from the game.
    config.game_main_transition = None

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = None

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = None

    ## Used when a game is loaded.
    config.after_load_transition = None

    ## Used when the window is shown.
    config.window_show_transition = None

    ## Used when the window is hidden.
    config.window_hide_transition = None


    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persisten information can be found by the init code.)
python early:
    config.save_directory = "Wanderer-1279766257"

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 80

    #########################################
    ## More customizations can go here.
    
    
init -2 python:        
    layout.imagemap_main_menu(
        "ui/menu_off.png",
        "ui/menu_on.png",
        [ (195, 489, 255, 530, "Start Game"),
          (260, 489, 310, 530, "Load Game"), 
          (320, 489, 375, 530, "Extras"),
          (385, 489, 470, 530, "Options"),
          (480, 489, 550, 530, "Credits"),
          (560, 489, 610, 530, "Quit") ]
        )
        
    layout.imagemap_yesno_prompt(
        "ui/yesno_off.png",
        "ui/yesno_off.png",
        "ui/yesno_over.png",
        [
            (250, 125, 325, 170, "Yes"),
            (475, 125, 550, 170, "No"),
        ],
        {
            layout.ARE_YOU_SURE : "ui/are_you_sure.png",
            layout.DELETE_SAVE : "ui/delete_save.png",
            layout.OVERWRITE_SAVE : "ui/overwrite_save.png",
            layout.LOADING : "ui/loading.png",
            layout.QUIT : "ui/quit.png",
            layout.MAIN_MENU : "ui/main_menu.png",
        }
    )
    
    style.yesno_prompt_text.xpos = 0.5
    style.yesno_prompt_text.ypos = 0.25
    style.yesno_prompt_text.xanchor = 0.5
 
