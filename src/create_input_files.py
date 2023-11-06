from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    # create_input_files(dataset='coco',
    #                    karpathy_json_path='../caption data/dataset_coco.json',
    #                    image_folder='caption data/',
    #                    captions_per_image=5,
    #                    min_word_freq=5,
    #                    output_folder='caption data/',
    #                    max_len=50)


    create_input_files(dataset='coco',
                       karpathy_json_path=r"D:\Partition\PROJECTS\__Personal\utd_task\CV-Task\CV-Task\descriptions.json",
                       image_folder=r"D:\Partition\PROJECTS\__Personal\utd_task\CV-Task\CV-Task\images\images",
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder= r"D:\Partition\PROJECTS\__Personal\utd_task\CV-Task\CV-Task",
                       max_len=50)
