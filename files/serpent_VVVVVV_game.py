from serpent.game import Game

from .api.api import VVVVVVAPI

from serpent.utilities import Singleton




class SerpentVVVVVVGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"

        kwargs["window_name"] = "VVVVVV"

        kwargs["app_id"] = "70300"
        kwargs["app_args"] = None

        super().__init__(**kwargs)

        self.api_class = VVVVVVAPI
        self.api_instance = None

        self.frame_transformation_pipeline_string = "RESIZE:640x480|GRAYSCALE"

        self.frame_width = 640
        self.frame_height = 480
        self.frame_channels = 0

        #query_sprite = Sprite("QUERY", image_data=query_image[])
        #self.viridian = self.sprite_identifier.identify(query_sprite, mode="SIGNATURE_COLORS")

    @property
    def screen_regions(self):
        regions = {
            "HP_AREA": (140, 0, 480, 500),
            "SCORE_AREA": (40, 0, 80, 140)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
