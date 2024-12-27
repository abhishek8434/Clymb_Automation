# utils/locators.py

def get_emotion_xpath(emotion_name):
    emotions = {
        "happy": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[1]/div/label/img',
        "angry": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[2]/div/label/img',
        "meh": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[2]/div/label/img',
        "sad": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[4]/div/label/img',
        "excited": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[5]/div/label/img',
        "fearful": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/fieldset/ul/li[6]/div/label/img',
    }
    return emotions.get(emotion_name, "Emotion not found!")


def get_slider_dict():
    slider = {
        "1": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[1]/ngx-slider-tooltip-wrapper[2]/div',
        "2": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[2]/ngx-slider-tooltip-wrapper[2]/div',
        "3": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[3]/ngx-slider-tooltip-wrapper[2]/div',
        "4": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[4]/ngx-slider-tooltip-wrapper[2]/div',
        "5": '/html/body/app-root/app-main-layout/main/app-home/section/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/ngx-slider/span[12]/span[5]/ngx-slider-tooltip-wrapper[2]/div',
    }
    return slider

# mood_utils.py

def get_mood_dict():
    mood = {
        "mood1": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][1]/*[name()='path'][3]",
        "mood2": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][1]/*[name()='path'][4]",
        "mood3": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][2]/*[name()='path'][3]",
        "mood4": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][2]/*[name()='path'][4]",
        "mood5": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][3]/*[name()='path'][3]",
        "mood6": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][3]/*[name()='path'][4]",
        "mood7": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][4]/*[name()='path'][3]",
        "mood8": "/html[1]/body[1]/ngb-modal-window[1]/div[1]/div[1]/app-emotion-wheel[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]/*[name()='g'][4]/*[name()='path'][4]",
    }
    return mood



