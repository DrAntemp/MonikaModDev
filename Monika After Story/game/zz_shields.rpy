# Module that contains both work-flow specific shield functions and
# generalized shield functions.
#

init python:
    # WORKFLOW-BASED

    # please add descriptions of workflows and what needs to be
    # enabled / disabled

    ######################### Core Disable ####################################
    # Not a workflow, just a specific set of shield functions that disable
    # and enable core interactions. Certain RenPy / DDLC-based interactions
    # may still work even when this shield is raised
    def mas_DropShield_core():
        """
        Enables:
            - Talk button + hotkey
            - Extra button + hotkey 
            - Music button + hotkey + volume keys + mute key
            - Play button + hotkey
            - Calendar overlay
            - Escape key
        """
        mas_HKDropShield()
        mas_OVLDropShield()
        enable_esc()


    def mas_RaiseShield_core():
        """
        Disables:
            - Talk button + hotkey
            - Extra button + hotkey
            - Music button + hotkey + volume keys + mute key
            - Play button + hotkey
            - Calendar overlay
            - Escape key
        """
        mas_HKRaiseShield()
        mas_OVLRaiseShield()
        disable_esc()


    #################### Allow Dialogue workflow ##############################
    # Used when Monika is speaking.
    def mas_DropShield_dlg():
        """
        Enables:
            - Talk button + hotkey
            - Extra button + hotkey
            - Play button + hotkey
            - Calendar overlay

        Unsets:
            - dialogue workflow flag

        Intended Flow:
            - Monika stops talking
        """
        store.mas_hotkeys.talk_enabled = True
        store.mas_hotkeys.extra_enabled = True
        store.mas_hotkeys.play_enabled = True
        store.hkb_button.talk_enabled = True
        store.hkb_button.extra_enabled = True
        store.hkb_button.play_enabled = True
        store.mas_globals.dlg_workflow = False
        mas_calDropOverlayShield()

    
    def mas_RaiseShield_dlg():
        """
        Disables:
            - Talk button + hotkey
            - Extra button + hotkey
            - Play button + hotkey
            - Calendar overlay

        Sets:
            - dialogue workflow flag

        Intended Flow:
            - Monika starts talking
        """
        store.mas_hotkeys.talk_enabled = False
        store.mas_hotkeys.extra_enabled = False
        store.mas_hotkeys.play_enabled = False
        store.hkb_button.talk_enabled = False
        store.hkb_button.extra_enabled = False
        store.hkb_button.play_enabled = False
        store.mas_globals.dlg_workflow = True
        mas_calRaiseOverlayShield()


    ################### Music Menu opened workflow ############################
    # Used when the music menu opens.
    def mas_DropShield_mumu():
        """
        Enables:
            - Talk button + hotkey
            - Extra button + hotkey
            - Music button
            - Play button + hotkey
            - Calendar overlay

        Intended Flow:
            - The Music menu is closed
        """
        store.mas_hotkeys.talk_enabled = True
        store.mas_hotkeys.extra_enabled = True
        store.mas_hotkeys.play_enabled = True
        mas_OVLDropShield()


    def mas_RaiseShield_mumu():
        """
        Disables:
            - Talk button + hotkey
            - Extra button + hotkey
            - Music button
            - Play button + hotkey
            - Calendar overlay           

        Intended Flow:
            - The Music menu is opened
        """
        store.mas_hotkeys.talk_enabled = False
        store.mas_hotkeys.extra_enabled = False
        store.mas_hotkeys.play_enabled = False
        mas_OVLRaiseShield()


    ################## Idle mode workflow #####################################
    # Used in idle mode
    def mas_DropShield_idle():
        """
        Enables:
            - Talk hotkey
            - Extra hotkey
            - Music hotkey
            - Play button + hotkey

        Intended Flow:
            - Idle mode ends
        """
        mas_HKDropShield()
        store.hkb_button.play_enabled = True


    def mas_RaiseShield_idle():
        """
        Disables:
            - Talk hotkey
            - Extra hotkey
            - Music hotkey
            - Play button + hotkey

        Intended Flow:
            - Idle mode starts
        """
        mas_HKRaiseShield()
        store.hkb_button.play_enabled = False


################################## GENERALIZED ################################
    # NOTE: only generalized functions that are mult-module encompassing
    # are allowed here. IF a generalized function is mostly related to 
    # a specific store/module, make it there. NOT here.

    ################## Enable / Disable Music Menu ############################
    # specifically for enabling and disabling the music menu
    def mas_MUMUDropShield():
        """
        Enables:
            - Music button + hotkey
            - Music Menu

        Intended Flow:
            - Whenever the music menu-based interactions need to be enabled
        """
        store.mas_hotkeys.music_enabled = True
        store.hkb_button.music_enabled = True
        store.songs.enabled = True


    def mas_MUMURaiseShield():
        """
        Disables:
            - Music button + hotkey
            - Music Menu

        Intended Flow:
            - Whenever the music menu-based interactions need to be disabled
        """
        store.mas_hotkeys.music_enabled = False
        store.hkb_button.music_enabled = False
        store.songs.enabled = False


    ################## dlg <-> idle transitions ###############################
    # specifically for transitioning between DLg and idle modes
    def mas_dlgToIdleShield():
        """
        Enables:
            - Talk button
            - Extra button
            - Calendar overlay

        Disables:
            - Music hotkey
        
        Unsets:
            - dialogue workflow flag

        Intended flow:
            - when transitioning from a dialogue workflow to idle mode
        """
        store.hkb_button.talk_enabled = True
        store.hkb_button.extra_enabled = True
        store.mas_hotkeys.music_enabled = False
        store.mas_globals.dlg_workflow = False
        mas_calDropOverlayShield()

    
    def mas_coreToIdleShield():
        """
        Enables:
            - Talk button
            - Extra button
            - Music button
            - Calendar overlay
            - Escape key

        Intended flow:
            - when transitiong from core sheilds to idle shields
        """
        store.hkb_button.talk_enabled = True
        store.hkb_button.extra_enabled = True
        store.hkb_button.music_enabled = True
        mas_calDropOverlayShield()
        enable_esc()


    def mas_mumuToIdleShield():
        """
        Enables:
            - Talk button
            - Extra button
            - Music button
            - songs
            - calendar overlay

        Intended Flow:
            - when transitioning from music menu to idle mode
        """
        store.hkb_button.talk_enabled = True
        store.hkb_button.extra_enabled = True
        store.hkb_button.music_enabled = True
        store.songs.enabled = True
        mas_calDropOverlayShield()
