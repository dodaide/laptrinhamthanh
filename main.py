from AudioEffects import AudioEffects

input_file = "input.wav"

# Tạo đối tượng AudioEffects
audio_effects = AudioEffects(input_file)

# Thêm hiệu ứng echo
audio_effects.add_echo("output_file_echo.wav", delay_ms=500, intensity=0.6)

# Lật ngược âm thanh
audio_effects.reverse_audio("output_file_reverse.wav")

# Thêm khoảng tĩnh lặng vào đầu file âm thanh
audio_effects.dangle_audio("output_file_dangle.wav", duration_ms=5000)
