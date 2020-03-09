using System;
using System.Management;
using System.Windows.Forms;

namespace RFGrid_GUI
{
    public partial class AvailablePorts : Form
    {

        public AvailablePorts()
        {

            InitializeComponent();

        }
        private MainWindow mainForm = null;
        public AvailablePorts(Form callingForm)
        {
            mainForm = callingForm as MainWindow;
            InitializeComponent();
        }


        private void RefreshButton_Click(object sender, EventArgs e)
        {
            getAvailablePorts();
        }


        const int EMPTY = 0;

        private void getAvailablePorts()
        {
            PortList.Items.Clear();
            ManagementScope connectionScope = new ManagementScope();
            SelectQuery serialQuery = new SelectQuery("SELECT * FROM Win32_SerialPort");
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(connectionScope, serialQuery);

            try
            {
                foreach (ManagementObject item in searcher.Get())
                {
                    string desc = item["Description"].ToString();
                    string deviceId = item["DeviceID"].ToString();

                    if (desc.Contains("Arduino"))
                    {
                        PortList.Items.Add(desc + " " + deviceId);
                    }


                }
                if (PortList.Items.Count == EMPTY)
                {
                    string info = "No Arduino COM Port Found.";
                    System.Windows.Forms.MessageBox.Show(info, "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }
            catch (ManagementException e)
            {
                MessageBox.Show(e.Message);
            }

        }

        private void SaveButtonPorts_Click(object sender, EventArgs e)
        {
            if (PortList.GetItemText(PortList.SelectedItem) != "")
            {

                this.mainForm.LabelText = (PortList.GetItemText(PortList.SelectedItem));
                mainForm.Text = mainForm.LabelText;
                System.Windows.Forms.MessageBox.Show("Selected Port: " + mainForm.LabelText, "Success", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                this.Close();
            }

        }

    }


}


