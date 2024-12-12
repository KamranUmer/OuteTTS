import outetts


def model_config_setting(languagetype,speakertype,inputtxt):
    model_config = outetts.HFModelConfig_v1(
        model_path="OuteAI/OuteTTS-0.2-500M",
        # language="en",  
        language=languagetype,  

    )

    interface = outetts.InterfaceHF(model_version="0.2", cfg=model_config)

    interface.print_default_speakers()
    # speaker = interface.load_default_speaker(name="male_1")
    speaker = interface.load_default_speaker(name=speakertype)


    output = interface.generate(
        # text="Speech synthesis is the artificial production of human speech. A computer system used for this purpose is called a speech synthesizer, and it can be implemented in software or hardware products.",
        text = inputtxt,
        temperature=0.1,
        repetition_penalty=1.1,
        max_length=4096,
        speaker=speaker,
    )

    output.save("outputsound.wav")
