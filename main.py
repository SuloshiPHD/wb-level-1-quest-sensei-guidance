scene.set_background_color(6)
# Use a splash screen at the beginning of your project
game.splash("My first coding project!")
# Create a sprite
mySprite = sprites.create(img("""
        . . . . f f f f . . . . . 
            . . f f f f f f f f . . . 
            . f f f f f f c f f f . . 
            f f f f f f c c f f f c . 
            f f f c f f f f f f f c . 
            c c c f f f e e f f c c . 
            f f f f f e e f f c c f . 
            f f f b f e e f b f f f . 
            . f 4 1 f 4 4 f 1 4 f . . 
            . f e 4 4 4 4 4 4 e f . . 
            . f f f e e e e f f f . . 
            f e f b 7 7 7 7 b f e f . 
            e 4 f 7 7 7 7 7 7 f 4 e . 
            e e f 6 6 6 6 6 6 f e e . 
            . . . f f f f f f . . . . 
            . . . f f . . f f . . . .
    """),
    SpriteKind.player)
# Set the sprites position every time the sprite image changes
mySprite.set_position(36, 60)
# Make the sprite say something every time the sprite image changes.
# 
# 
mySprite.say("Hello World!")
# Play a sound every time the sprite image changes.
# 
music.play(music.melody_playable(music.power_up),
    music.PlaybackMode.UNTIL_DONE)
# Set the background color every time the sprite image changes.
scene.set_background_color(3)
# Change the Sprite image
mySprite.set_image(img("""
    . . . . f f f f f . . . . . . . 
        . . . f e e e e e f . . . . . . 
        . . f d d d d e e e f . . . . . 
        . . f d d f d d e e f f . . . . 
        . c d d d f d d e e d d f . . . 
        c d e e d d d d e e b d c . . . 
        c d d d d c d d e e b d c . . . 
        c f f f f d d d e e f c f . . . 
        . f b d f f f e e e e f . . . . 
        . f d d f e f f f e e f . . . . 
        . . f f f e e e e f f f . f f . 
        . . f e e f e e e e f f . e f . 
        . f f e e e f f f f f f f e f . 
        . f b d f e e f b b f f f e f . 
        . f d d f f e e d d b f f f f . 
        . f f f f f f f f f f f f f . .
"""))
mySprite.set_position(127, 60)
mySprite.say("I love coding!")
music.play(music.melody_playable(music.beam_up),
    music.PlaybackMode.UNTIL_DONE)
scene.set_background_color(7)
mySprite.set_image(img("""
    . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . b 5 5 b . . . 
        . . . . . . b b b b b b . . . . 
        . . . . . b b 5 5 5 5 5 b . . . 
        . b b b b b 5 5 5 5 5 5 5 b . . 
        . b d 5 b 5 5 5 5 5 5 5 5 b . . 
        . . b 5 5 b 5 d 1 f 5 d 4 f . . 
        . . b d 5 5 b 1 f f 5 4 4 c . . 
        b b d b 5 5 5 d f b 4 4 4 4 b . 
        b d d c d 5 5 b 5 4 4 4 4 4 4 b 
        c d d d c c b 5 5 5 5 5 5 5 b . 
        c b d d d d d 5 5 5 5 5 5 5 b . 
        . c d d d d d d 5 5 5 5 5 d b . 
        . . c b d d d d d 5 5 5 b b . . 
        . . . c c c c c c c c b b . . .
"""))
mySprite.set_position(71, 30)
mySprite.say("I'm excited to learn!")
music.play(music.melody_playable(music.pew_pew),
    music.PlaybackMode.UNTIL_DONE)
# Use a screen effect at the end of your project.
effects.hearts.start_screen_effect()