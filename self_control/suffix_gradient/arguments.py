import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--model_name_or_path", type=str, default="meta-llama/Llama-2-7b-chat-hf")
parser.add_argument("--attribute", type=str, default="happy", help="The attribute of the seed queries to generate")
parser.add_argument("--data_path", type=str, default=None, help="Path of a dataset")
parser.add_argument("--output_name", type=str, default=None, help="Name of the output file")
parser.add_argument("--resume_from", type=str, default=None, help="Resume from a previous data checkpoint")
parser.add_argument("--max_num_data", type=int, default=300, help="Max number of data item")
parser.add_argument("--start_from_idx", type=int, default=0, help="Start index of the data")
parser.add_argument("--batchsize", type=int, default=3, help="Batch size")
parser.add_argument("--epoch", type=int, default=1, help="Epoch of data generation, should be used with sampling")
parser.add_argument("--max_norm", type=int, default=100, help="Filter gradients by their norms")

# control_generate
parser.add_argument("--search", action="store_true")
parser.add_argument("--init_coeff", type=float, default=-0.5, help="Coefficient for control. Will serve as the initial coeff if search=True")
parser.add_argument("--iteration", type=int, default=1, help="Number of iterations of control")
parser.add_argument("--random_seed", type=int, default=42, help="Random seed")
parser.add_argument("--do_sample", action="store_true")
parser.add_argument("--temperature", type=float, default=None, help="Temperature")
parser.add_argument("--max_new_tokens", type=int, default=50, help="Max new tokens")
parser.add_argument("--return_hiddens", action="store_true")
args = parser.parse_args()