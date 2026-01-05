from assets import Sprites


class RendererBlockBreakingStage:
    @staticmethod
    def render(screen, block, pos):
        if block.hardness < block.max_hardness and Sprites.BREAKING_STAGES:
            progress = (block.max_hardness - block.hardness) / block.max_hardness
            stage_index = int(progress * len(Sprites.BREAKING_STAGES))
            stage_index = min(stage_index, len(Sprites.BREAKING_STAGES) - 1)

            crack_surf = Sprites.BREAKING_STAGES[stage_index]
            screen.blit(crack_surf, pos.to_tuple())
