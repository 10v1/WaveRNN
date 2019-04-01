# CONFIG
wav_path = '/path/to/wav_files/'
data_path = 'data/'
model_id = '9bit_mulaw'

#------------------------------------------------------------------------------------------------------------------#

# DSP SETTINGS FOR ALL MODELS
sample_rate = 22050
n_fft = 2048
fft_bins = n_fft // 2 + 1
num_mels = 80
hop_length = 275                # 12.5ms - in line with Tacotron 2 paper
win_length = 1100               # 50ms - same as above
fmin = 40
min_level_db = -100
ref_level_db = 20
bits = 9                        # bit depth of signal
mu_law = True                   # Recommended to suppress noise
peak_norm = False

#------------------------------------------------------------------------------------------------------------------#

# WAVERNN/VOCODER MODEL
voc_upsample_factors = (5, 5, 11)   # NB - this needs to correctly factorise hop_length - triple-check if modifying
voc_rnn_dims = 512
voc_fc_dims = 512
voc_compute_dims = 128
voc_res_out_dims = 128
voc_res_blocks = 10

# WAVERNN/VOCODER TRAINING
voc_batch_size = 32
voc_lr = 1e-4
voc_checkpoint_every = 25_000
voc_gen_at_checkpoint = 5           # number of samples to generate at each checkpoint
voc_total_steps = 500_000           # Total number of training steps
voc_test_samples = 50               # How many unseen samples to put aside for testing
voc_pad = 2                         # this will pad the input so that the resnet conv can 'see' wider than input length
voc_seq_len = hop_length * 5        # must be a multiple of hop_length

# WAVERNN/VOCODER GENERATING
voc_gen_batched = True              # very fast (realtime+) single utterance batched generation
voc_target = 11_000                 # target number of samples to be generated in each batch entry
voc_overlap = 550                   # number of samples for crossfading between batches

#------------------------------------------------------------------------------------------------------------------#

# TACOTRON/TTS MODEL



# TACOTRON/TTS TRAINING

#------------------------------------------------------------------------------------------------------------------#

