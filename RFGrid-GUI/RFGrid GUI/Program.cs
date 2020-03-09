using System;
using System.Windows.Forms;

namespace RFGrid_GUI
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {

            bool running = false;

            using (System.Threading.Mutex mtex = new System.Threading.Mutex(true, "RFGrid GUI", out running))
            {
                if (running)
                {
                    Application.EnableVisualStyles();
                    Application.SetCompatibleTextRenderingDefault(false);
                    Application.Run(new MainWindow());
                    mtex.ReleaseMutex();
                }
                else
                {
                    MessageBox.Show("RFGrid GUI is already running.");
                }
            }
        }
    }
}
