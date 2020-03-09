using System;
using System.IO;
using System.IO.Ports;
using System.Windows.Forms;


namespace RFGrid_GUI
{
    public partial class MainWindow : Form
    {
        //Globals
        string selectedGameGlobal = "";
        SerialPort serialPort = new SerialPort();
        System.Media.SoundPlayer player = new System.Media.SoundPlayer();
        const int dispCalib = 1;
        const int backgroundCalib = 2;
        const int launch = 3;

        string original_dir = Directory.GetCurrentDirectory();
        const int RX_UPDATE = 0x00;
        const int RX_SYNC = 0x0F;

        public MainWindow()
        {
            InitializeComponent();
            backgroundCalibPictureBox.Image = Properties.Resources.defaultPicture;
            ApplicationsRefreshButton_Click(null, new EventArgs());

        }



        private void ImageButton_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog()
            {
                FileName = "Select an image file",
                Filter = "Image files (*.png)|*.png",
                Title = "Choose Image file"
            };

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                imageTextBox.Text = openFileDialog1.FileName;
                tagCreatorPreviewBox.ImageLocation = imageTextBox.Text;
            }

        }

        private void SaveButton_Click(object sender, EventArgs e)
        {
            string data = "";
            bool flag = false;
            bool duplicate_id = false;
            string new_image_path = "";
            string new_sound_path = "";
            string new_sound_second_path = "";

            //Tag ID must be present
            if (!(String.IsNullOrEmpty((string)tagBox.Text)))
            {
                //Check first sound textbox
                if (((String.IsNullOrEmpty((string)soundTextBox.Text))))
                {
                    soundTextBox.Text = "";
                    new_sound_path = "";
                }
                else
                {
                    new_sound_path = "./sounds/" + Path.GetFileName(soundTextBox.Text);
                }
                if (((String.IsNullOrEmpty((string)secondSoundTextBox.Text))))
                {
                    secondSoundTextBox.Text = "";
                    new_sound_second_path = "";
                }
                else
                {
                    new_sound_second_path = "./sounds/" + Path.GetFileName(secondSoundTextBox.Text);
                }

                if ((!(String.IsNullOrEmpty((string)imageTextBox.Text))))
                {
                    new_image_path = "./images/objects/" + Path.GetFileName(imageTextBox.Text);
                }


                data = tagBox.Text + "," + new_image_path + "," + new_sound_path + "," + new_sound_second_path;
                flag = true;
            }
            else System.Windows.Forms.MessageBox.Show("Tag ID field cannot be empty!", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);

            if (flag)
            {
                //Need to agree on where to copy. but this works right now.
                string configs_path = Directory.GetCurrentDirectory() + "\\applications\\" + selectedGameGlobal + "\\configs\\";
                string objects_path = Directory.GetCurrentDirectory() + "\\applications\\" + selectedGameGlobal + "\\images\\objects\\";
                string sounds_path = Directory.GetCurrentDirectory() + "\\applications\\" + selectedGameGlobal + "\\sounds\\";
                string path = Directory.GetCurrentDirectory() + "\\applications\\" + selectedGameGlobal + "\\configs\\tags.rfgridtag";
                if (Directory.Exists(configs_path))
                {
                    if (File.Exists(path))
                    {
                        //Have to go through the file and read every line.
                        //Then if it exists, edit that line and re-write the file.
                        //Otherwise, it is a new ID and just append it to the file.
                        string[] arrLine = System.IO.File.ReadAllLines(path);
                        string[] IDs = new string[] { };
                        for (var i = 0; i < arrLine.Length; i += 1)
                        {
                            string line = arrLine[i];
                            IDs = line.Split(',');
                            if (IDs[0] == tagBox.Text)
                            {
                                arrLine[i] = data;
                                duplicate_id = true;
                            }

                        }
                        if (!duplicate_id)
                            System.IO.File.AppendAllText(path, data + Environment.NewLine);
                        else System.IO.File.WriteAllLines(path, arrLine);

                    }
                    else
                    {

                        System.IO.File.WriteAllText(path, data + Environment.NewLine);

                    }
                    if (soundTextBox.Text != "" && !File.Exists(objects_path + Path.GetFileName(soundTextBox.Text)))
                        System.IO.File.Copy(soundTextBox.Text, sounds_path + Path.GetFileName(soundTextBox.Text), true);
                    if (secondSoundTextBox.Text != "" && !File.Exists(objects_path + Path.GetFileName(secondSoundTextBox.Text)))
                        System.IO.File.Copy(secondSoundTextBox.Text, sounds_path + Path.GetFileName(secondSoundTextBox.Text), true);
                    if (imageTextBox.Text != "" && !File.Exists(objects_path + Path.GetFileName(imageTextBox.Text)))
                        System.IO.File.Copy(imageTextBox.Text, objects_path + Path.GetFileName(imageTextBox.Text), true);
                    System.Windows.Forms.MessageBox.Show("Tag is sucessfully created.", "Success", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                }
                else System.Windows.Forms.MessageBox.Show("Make sure this executable is located in the rfgrid folder.",
                    "Error!", MessageBoxButtons.OK, MessageBoxIcon.Error);

            }
            loadTagInfo();
        }

        private void ClearButton_Click(object sender, EventArgs e)
        {
            tagBox.Text = null;
            imageTextBox.Text = null;
            soundTextBox.Text = null;
            secondSoundTextBox.Text = null;
        }

        private void SoundButton_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog()
            {
                FileName = "Select a sound file",
                Filter = "Sound files (*.wav)|*.wav",
                Title = "Choose Sound file"
            };

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                soundTextBox.Text = openFileDialog1.FileName;
            }
        }


        private void ChooseCOMToolStripMenuItem_Click(object sender, EventArgs e)
        {
            AvailablePorts to = new AvailablePorts(this);
            to.Show();

        }

        public string LabelText
        {
            get { return portTextLabel.Text; }
            set { portTextLabel.Text = value; }
        }

        private void DisplayInfoButton_Click(object sender, EventArgs e)
        {
            System.Windows.Forms.MessageBox.Show("rfgrid device dimensions.\nExample: 4x4, 8x8, 12x12,16x16.", "Information", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }


        

        private void DispCalibrateButton_Click(object sender, EventArgs e)
        {
            if (loadedConfigurationLabel.Text != "N/A")
            {
                Directory.SetCurrentDirectory(Directory.GetCurrentDirectory() + "\\applications\\" + selectedGameGlobal);
                string filePath = "rfgridDispCalib.py";
                string args = dispCalibXBox.Text + "x" + dispCalibYBox.Text;
                run_cmd(filePath, args, dispCalib);
                Directory.SetCurrentDirectory(original_dir);
            }
            else
            {
                System.Windows.Forms.MessageBox.Show("Please load an Application first.",
                    "Error!", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }


        private bool isRunning = false;
        private void InstallModulesToolStripMenuItem_Click(object sender, EventArgs e)
        {

            if (isRunning)
            {
                System.Windows.Forms.MessageBox.Show("Installing python modules..",
                    "Warning!", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            /* Multi-tasking is possible while installing modules.*/
            System.Threading.Thread workerThread = new System.Threading.Thread(
                new System.Threading.ThreadStart(() =>
                {
                    isRunning = true;
                    debugTextBox.AppendText("Please wait while installing required python packages..");
                    string filePath = "";
                    if (!File.Exists(Directory.GetCurrentDirectory() + @"\python\python-3.7.6\Scripts\pip.exe"))
                    {
                        filePath = Directory.GetCurrentDirectory() + @"\python\setup\get-pip.py";
                        run_cmd(filePath, "", dispCalib);


                        /* This requires adminisrator priveleges */
                        filePath = Directory.GetCurrentDirectory() + @"\python\python-3.7.6\Scripts\Lib\site-packages" + ";" + Directory.GetCurrentDirectory() + @"\python\python-3.7.6\Scripts" + ";" + Directory.GetCurrentDirectory() + @"\python\python-3.7.6";
                        System.Environment.SetEnvironmentVariable("PATH", filePath, EnvironmentVariableTarget.Machine);
                    }
                    else
                    {
                        filePath = Directory.GetCurrentDirectory() + @"\python\setup\modules.py";
                        run_cmd(filePath, "", dispCalib);
                    }
                    isRunning = false;
                }
                ));
            workerThread.Start();
        }


        private void run_cmd(string cmd, string args, int type)
        {

            string result;

            System.Diagnostics.ProcessStartInfo start = new System.Diagnostics.ProcessStartInfo();
            start.FileName = System.AppDomain.CurrentDomain.BaseDirectory + @"python\python-3.7.6\python.exe";
            switch (type)
            {
                case dispCalib:
                    args = args;
                    break;
                case backgroundCalib:

                    args = "default.jpg";
                    break;
                case launch:
                    args = selectedGameGlobal + " " + args;
                    break;
            }
            debugTextBox.AppendText(args);
            start.Arguments = string.Format(@"""{0}"" {1}", cmd, args);
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            start.RedirectStandardError = true;
            start.CreateNoWindow = true;
            using (System.Diagnostics.Process process = System.Diagnostics.Process.Start(start))
            {
                using (System.IO.StreamReader reader = process.StandardOutput)
                {
                    string stderr = process.StandardError.ReadToEnd();
                    debugTextBox.AppendText(">" + stderr + "\n");
                    result = reader.ReadToEnd();
                    debugTextBox.AppendText(">" + result + "\n");
                }
            }
        }

        private void ExitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            System.Windows.Forms.Application.Exit();
        }

        private void BackgroundImgButton_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog()
            {
                FileName = "Select an image file",
                Filter = "Image files (*.jpg)|*.jpg",
                Title = "Choose image file"
            };

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                backgroundImgTextBox.Text = openFileDialog1.FileName;
                backgroundCalibPictureBox.ImageLocation = backgroundImgTextBox.Text;
                backgroundCalibPictureBox.SizeMode = PictureBoxSizeMode.StretchImage;
            }
        }

        private void BackgroundCalibButton_Click(object sender, EventArgs e)
        {
            if (loadedConfigurationLabel.Text != "N/A")
            {
                string filePath = "rfgridBackgroundCalib.py";
                Directory.SetCurrentDirectory(Directory.GetCurrentDirectory() + "\\applications\\" + selectedGameGlobal);
                if (backgroundImgTextBox.Text == "default.jpg")
                {
                    ; //do nothing..
                }
                else
                {

                    string backgrounds_path = Directory.GetCurrentDirectory() + "\\images\\backgrounds\\";

                    if (File.Exists(backgroundImgTextBox.Text))
                    {
                        System.IO.File.Copy(backgroundImgTextBox.Text, backgrounds_path + "default.jpg", true);

                    }
                }
                run_cmd(filePath, "", backgroundCalib);
                Directory.SetCurrentDirectory(original_dir);

            }
            else
            {
                System.Windows.Forms.MessageBox.Show("Please load an Application first.",
                    "Error!", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }


        private void AboutToolStripMenuItem_Click(object sender, EventArgs e)
        {
            string info = "ECED 4900-4901 Senior Year Project 2019-2020\n\n" +
                          "Project: Interactive RFID Display\n\n" +
                          "Members\n" +
                          "\n" +
                          "- Burak Ozter\n" +
                          "- Mark Hooper";
            System.Windows.Forms.MessageBox.Show(info, "About", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }







        private void TagGetIdButton_Click(object sender, EventArgs e)
        {

            if (portTextLabel.Text != "NA")
            {
                if ((dispCalibXBox.Text == "") && (dispCalibYBox.Text == ""))
                {
                    dispCalibXBox.Text = "8";
                    dispCalibYBox.Text = "8";
                }
                string info = "Place the tag on the 0,0 tile.(top left)\n\n" +
              "You do not need to click this button again to scan a tag.";
                System.Windows.Forms.MessageBox.Show(info, "About", MessageBoxButtons.OK, MessageBoxIcon.Information);


                string[] arr = portTextLabel.Text.Split(' ');
                int index = arr.Length;
                /* Initialize set-up here*/

                serialPort.PortName = arr[index - 1];
                serialPort.BaudRate = 9600;
                serialPort.DataBits = 8;
                serialPort.Parity = Parity.None;
                serialPort.StopBits = StopBits.One;
                serialPort.RtsEnable = false;
                serialPort.DtrEnable = false;

                serialPort.Open();
                serialPort.DiscardInBuffer();
                serialPort.DiscardOutBuffer();
                TX_Sync(serialPort, dispCalibXBox.Text, dispCalibYBox.Text);


                serialPort.DataReceived += new
     SerialDataReceivedEventHandler(port_DataReceived);

                tagGetIdButton.Enabled = false;

            }
            else
            {
                System.Windows.Forms.MessageBox.Show("No COM Port is Selected.",
                   "Error!", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

        }


        private void port_DataReceived(object sender,
                                 SerialDataReceivedEventArgs e)
        {

            SerialPort sp = (SerialPort)sender;

            this.Invoke((MethodInvoker)delegate
            {
                byte[] cmd = new byte[1];
                byte[] args = new byte[6];

                sp.Read(cmd, 0, 1); //READ ONE BYTE
                System.Threading.Thread.Sleep(50);
                switch (cmd[0])
                {
                    case RX_SYNC:
                        sp.Read(args, 0, 3);
                        //debugTextBox.AppendText("\nSynced.");
                        if (args[0] == 0)
                        {
                            //Resync here
                        }
                        System.Threading.Thread.Sleep(50);
                        break;
                    case RX_UPDATE:
                        //debugTextBox.AppendText("\nUpdate Received.");
                        sp.Read(args, 0, 6);
                        byte[] idBytes = new byte[4];
                        idBytes[3] = args[0];
                        idBytes[2] = args[1];
                        idBytes[1] = args[2];
                        idBytes[0] = args[3];
                        UInt32 tagID = BitConverter.ToUInt32(idBytes, 0);
                        if ((args[4] == 0x00) && (args[5] == 0x00) && (tagID != 0))
                        {
                            tagBox.Text = tagID.ToString();
                        }

                        byte[] TX_UPDATE = new byte[7];
                        TX_UPDATE[0] = 0xF0;
                        TX_UPDATE[1] = args[0];
                        TX_UPDATE[2] = args[1];
                        TX_UPDATE[3] = args[2];
                        TX_UPDATE[4] = args[3];
                        TX_UPDATE[5] = args[4];
                        TX_UPDATE[6] = args[5];
                        sp.Write(TX_UPDATE, 0, 7);
                        System.Threading.Thread.Sleep(50);
                        break;


                }

            });
            System.Threading.Thread.Sleep(150);

        }



        private void TX_Sync(SerialPort serialPort, string device_x, string device_y)
        {
            //send sync here..
            byte x = Convert.ToByte(Int16.Parse(device_x));
            byte y = Convert.ToByte(Int16.Parse(device_y));
            var sync = new byte[] { 0xFF, 0x01, x, y }; //SYNC CMD= 0xFF , START BYTE= 0x01, XMAX = 0x08, YMAX = 0x08
            serialPort.Write(sync, 0, sync.Length);
        }


        public void ApplicationsRefreshButton_Click(object sender, EventArgs e)
        {
            ApplicationsList.Items.Clear();

            string applications_path = Directory.GetCurrentDirectory() + "\\applications";
            if (Directory.Exists(applications_path))
            {
                string[] files = Directory.GetDirectories(applications_path);
                foreach (string fileName in files)
                {
                    if (!(Path.GetFileName(fileName) == "defaultAssets"))
                    {
                        ApplicationsList.Items.Add(Path.GetFileName(fileName));
                    }
                }
                ApplicationsList.Sorted = true;
            }
            else
            {
                System.Windows.Forms.MessageBox.Show("Applications folder not found",
                       "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);

            }


        }

        private void createNewApplicationButton_Click(object sender, EventArgs e)
        {
            NewGameForm to = new NewGameForm(this);
            to.Show();

        }


        public void DirectoryCopy(string sourceFolder, string destination)
        {

            DirectoryInfo dir = new DirectoryInfo(sourceFolder);
            DirectoryInfo[] dirs = dir.GetDirectories();

            // If the destination directory doesn't exist, create it.
            if (!Directory.Exists(destination))
            {
                Directory.CreateDirectory(destination);
            }


            FileInfo[] files = dir.GetFiles();
            foreach (FileInfo file in files)
            {
                string temppath = Path.Combine(destination, file.Name);
                file.CopyTo(temppath, true);
            }

            // If copying subdirectories, copy them and their contents to new location.
            foreach (DirectoryInfo subdir in dirs)
            {
                string temppath = Path.Combine(destination, subdir.Name);
                DirectoryCopy(subdir.FullName, temppath);
            }

        }



        private void openExistingApplicationButton_Click(object sender, EventArgs e)
        {
            selectedGameGlobal = ApplicationsList.GetItemText(ApplicationsList.SelectedItem);
            DialogResult result = System.Windows.Forms.MessageBox.Show("Application " + "\"" + selectedGameGlobal + "\"" + " is sucessfully loaded.",
      "Info", MessageBoxButtons.OK, MessageBoxIcon.Information);
            loadedConfigurationLabel.Text = selectedGameGlobal;
            backgroundCalibPictureBox.ImageLocation = Directory.GetCurrentDirectory() + "\\applications\\" + selectedGameGlobal + "\\images\\backgrounds\\default.jpg";
            loadTagInfo();

        }

        private void loadTagInfo()
        {
            string tagConfigPath = original_dir + @"\applications\" + selectedGameGlobal + @"\configs\tags.rfgridtag";
            tagInfoListView.Items.Clear();
            if (File.Exists(tagConfigPath))
            {

                int i = 0;
                ImageList imgs = new ImageList();
                imgs.ImageSize = new System.Drawing.Size(40, 40);
                tagInfoListView.SmallImageList = imgs;

                string[] lines = System.IO.File.ReadAllLines(tagConfigPath);
                foreach (string line in lines)
                {
                    var parsed_line = line.Split(',');
                    string[] imageName = Path.GetFileName(parsed_line[1]).Split('.');
                    string[] entranceSoundName = Path.GetFileName(parsed_line[2]).Split('.');
                    string[] updateSoundName = Path.GetFileName(parsed_line[3]).Split('.');
                    parsed_line[1] = imageName[0];
                    parsed_line[2] = entranceSoundName[0];
                    parsed_line[3] = updateSoundName[0];

                    if (parsed_line[1].Length != 0) 
                    {
                        imgs.Images.Add(parsed_line[1], System.Drawing.Image.FromFile(original_dir + @"\applications\" + selectedGameGlobal + @"\images\objects\" + imageName[0] + ".png"));
                        tagInfoListView.Items.Add(new ListViewItem(parsed_line) { ImageIndex = i });
                        i++;

                    }
                    else
                    {
                        tagInfoListView.Items.Add(new ListViewItem(parsed_line));
                    }

                }


            }
        }

        private void SecondSoundButton_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog()
            {
                FileName = "Select a sound file",
                Filter = "Sound files (*.wav)|*.wav",
                Title = "Choose Sound file"
            };

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                secondSoundTextBox.Text = openFileDialog1.FileName;
            }
        }

        private void DeleteApplicationButton_Click(object sender, EventArgs e)
        {
            string selected = ApplicationsList.GetItemText(ApplicationsList.SelectedItem);
            string selected_path = Directory.GetCurrentDirectory() + @"\applications\" + selected;
            DialogResult result = System.Windows.Forms.MessageBox.Show("Are you sure to delete " + "\"" + selected + "\"" + " ?",
       "Warning", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);
            if (result == DialogResult.Yes)
            {
                DeleteFolder(selected_path);
                result = System.Windows.Forms.MessageBox.Show("Application " + "\"" + selected + "\"" + "is sucessfully deleted.",
                       "Information", MessageBoxButtons.OK, MessageBoxIcon.Information);
                if (result == DialogResult.OK)
                {
                    ApplicationsRefreshButton_Click(DeleteApplicationButton, e);
                    tagInfoListView.Items.Clear();
                    selectedGameGlobal = "N/A";
                    loadedConfigurationLabel.Text = selectedGameGlobal;

                }
            }

        }

        private void DeleteFolder(string sourceFolder)
        {
            DirectoryInfo directoryInfo = new DirectoryInfo(sourceFolder);
            DirectoryInfo[] dirs = directoryInfo.GetDirectories();

            foreach (FileInfo file in directoryInfo.GetFiles())
            {
                file.Delete();
            }

            foreach (DirectoryInfo subfolder in dirs)
            {
                DeleteFolder(subfolder.FullName);
            }
            Directory.Delete(sourceFolder);
        }

        private void LaunchButton_Click(object sender, EventArgs e)
        {
            if (loadedConfigurationLabel.Text != "N/A")
            {
                serialPort.Close();
                string filePath = Directory.GetCurrentDirectory() + "\\applications\\" + selectedGameGlobal;
                string gameFile = Directory.GetCurrentDirectory() + "\\applications\\" + selectedGameGlobal + @"\" + selectedGameGlobal + ".py";
                Directory.SetCurrentDirectory(filePath);
                run_cmd(gameFile, null, launch);
                Directory.SetCurrentDirectory(original_dir);
            }
            else
            {
                System.Windows.Forms.MessageBox.Show("Please load an Application first.",
                    "Error!", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

        }


        /* Accepts Numbers Only */
        private void DispCalibXBox_TextChanged(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar))
            {
                e.Handled = true;
            }
        }



        private void DispCalibYBox_TextChanged(object sender, KeyPressEventArgs e)
        {
            if (!char.IsControl(e.KeyChar) && !char.IsDigit(e.KeyChar))
            {
                e.Handled = true;
            }
        }

        private void EntranceSoundPlayButton_Click(object sender, EventArgs e)
        {
            string sound_path = soundTextBox.Text;
            if (File.Exists(sound_path))
            {
                player.SoundLocation = (sound_path);
                player.Play();
            }
            else
            {
                System.Windows.Forms.MessageBox.Show("Sound file not found.",
                    "Error!", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void UpdateSoundPlayButton_Click(object sender, EventArgs e)
        {
            string sound_path = secondSoundTextBox.Text;
            if (File.Exists(sound_path))
            {
                player.SoundLocation = (sound_path);
                player.Play();
            }
            else
            {
                System.Windows.Forms.MessageBox.Show("Sound file not found.",
                    "Error!", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void TagInfoListView_SelectedIndexChanged(object sender, EventArgs e)
        {

            if (tagInfoListView.SelectedItems.Count > 0)
            {
                tagBox.Text = tagInfoListView.SelectedItems[0].Text;
                if (tagInfoListView.SelectedItems[0].SubItems[2].Text.Length != 0)
                {
                    soundTextBox.Text = Directory.GetCurrentDirectory() + @"\applications\" + selectedGameGlobal + @"\sounds\" + tagInfoListView.SelectedItems[0].SubItems[2].Text + ".wav";
                }
                else
                {
                    soundTextBox.Text = " ";
                }
                if (tagInfoListView.SelectedItems[0].SubItems[3].Text.Length != 0)
                {
                    secondSoundTextBox.Text = Directory.GetCurrentDirectory() + @"\applications\" + selectedGameGlobal + @"\sounds\" + tagInfoListView.SelectedItems[0].SubItems[3].Text + ".wav";
                }
                else
                {
                    secondSoundTextBox.Text = " ";
                }
            }
        }

        private void StopPlayingButton_Click(object sender, EventArgs e)
        {
            player.Stop();
        }
    }
}
