import os.path
from data.base_dataset import BaseDataset, get_params, get_transform
from data.utils import load_image
from data.image_folder import make_dataset
from PIL import Image


class AlignedDataset(BaseDataset):
    """A dataset class for paired image dataset.

<<<<<<< HEAD
    It assumes that the directories '/path/to/data/trainA' and '/path/to/data/trainB' contain image pairs with the same names.
    During test time, you need to prepare directories '/path/to/data/testA' and '/path/to/data/testB'.
=======
    It assumes that the directory '/path/to/data/train' contains image pairs in the form of {A,B}.
    During test time, you need to prepare a directory '/path/to/data/test'.
>>>>>>> 7d7dd98 (dingkang branch)
    """

    def __init__(self, opt, phase):
        """Initialize this dataset class.

        Parameters:
            opt (Option class) -- stores all the experiment flags; needs to be a subclass of BaseOptions
        """
        BaseDataset.__init__(self, opt, phase)
<<<<<<< HEAD

        self.A_paths = sorted(
            make_dataset(self.dir_A, opt.data_max_dataset_size)
        )  # load images from '/path/to/data/trainA'
        self.B_paths = sorted(
            make_dataset(self.dir_B, opt.data_max_dataset_size)
        )  # load images from '/path/to/data/trainB'

        if len(self.A_paths) != len(self.B_paths):
            raise Exception(
                "aligned dataset: domain A and domain B should have the same number of images"
            )
=======
        self.dir_AB = os.path.join(opt.dataroot, opt.phase)  # get the image directory
        self.AB_paths = sorted(
            make_dataset(self.dir_AB, opt.data_max_dataset_size)
        )  # get image paths
        assert (
            self.opt.data_load_size >= self.opt.data_crop_size
        )  # crop_size should be smaller than the size of loaded image
>>>>>>> 7d7dd98 (dingkang branch)

    def __getitem__(self, index):
        """Return a data point and its metadata information.

        Parameters:
            index - - a random integer for data indexing

        Returns a dictionary that contains A, B, A_paths and B_paths
            A (tensor) - - an image in the input domain
            B (tensor) - - its corresponding image in the target domain
            A_paths (str) - - image paths
            B_paths (str) - - image paths (same as A_paths)
        """
<<<<<<< HEAD
        # read a pair of images given a random integer index
        A_path = self.A_paths[index]
        B_path = self.B_paths[index]
        A = Image.open(A_path).convert("RGB")
        B = Image.open(B_path).convert("RGB")
=======
        # read a image given a random integer index
        AB_path = self.AB_paths[index]
        AB = load_image(AB_path)
        # split AB image into A and B
        w, h = AB.size
        w2 = int(w / 2)
        A = AB.crop((0, 0, w2, h))
        B = AB.crop((w2, 0, w, h))
>>>>>>> 7d7dd98 (dingkang branch)

        # apply the same transform to both A and B
        transform_params = get_params(self.opt, A.size)
        A_transform = get_transform(
            self.opt, transform_params, grayscale=(self.input_nc == 1)
        )
        B_transform = get_transform(
            self.opt, transform_params, grayscale=(self.output_nc == 1)
        )
<<<<<<< HEAD
        A = A_transform(A)
        B = B_transform(B)

        return {"A": A, "B": B, "A_img_paths": A_path, "B_img_paths": B_path}

    def __len__(self):
        """Return the total number of images in the dataset."""
        return len(self.A_paths)
=======

        A = A_transform(A)
        B = B_transform(B)

        return {"A": A, "B": B, "A_img_paths": AB_path, "B_img_paths": AB_path}

    def __len__(self):
        """Return the total number of images in the dataset."""
        return len(self.AB_paths)
>>>>>>> 7d7dd98 (dingkang branch)
