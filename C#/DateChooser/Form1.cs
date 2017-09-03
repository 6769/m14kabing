using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace DateChooser
{
    public partial class Form1 : Form
    {
        private DateTime aDateTime = new DateTime(1970, 1, 1);
        private const string HEX_HEADER = "0x";
        enum STATUE
        {
            NORMAL,ERROR
        }
        public Form1()
        {
            InitializeComponent();
            setupAllTimes(dateTimePicker1.Value.ToFileTimeUtc());
        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {
            var t = dateTimePicker1.Value;
            setupAllTimes(t.ToFileTimeUtc());
        }

        private void setupAllTimes(long tm)//accept C# time presentation;
        {
            var  t=DateTime.FromFileTimeUtc(tm);
            double utct = (t - aDateTime).TotalSeconds;
            long utctL = (long)utct;

            dateTimePicker1.Value = t;
            tbx_decmal.Text = utctL.ToString();
            tbx_hexval.Text = HEX_HEADER+utctL.ToString("X");
            toolStripStatusLabel1.Text = STATUE.NORMAL.ToString();
        }

        private void tbx_decmal_TextChanged(object sender, EventArgs e)
        {
            string decs = tbx_decmal.Text;
            try
            {
                long decL = long.Parse(decs);
                TimeSpan span=new TimeSpan(decL*1000*10000);
                DateTime dt = aDateTime + span;
                setupAllTimes(dt.ToFileTimeUtc());


            }
            catch (Exception exp)
            {
                //pass
                toolStripStatusLabel1.Text = STATUE.ERROR.ToString();
            }
        }

        private void tbx_hexval_TextChanged(object sender, EventArgs e)
        {
            string hexs = tbx_hexval.Text.ToUpper().Replace('X', '0');
            try
            {
                long hexL = long.Parse(hexs,System.Globalization.NumberStyles.HexNumber);
                TimeSpan span = new TimeSpan(hexL * 1000 * 10000);
                DateTime dt = aDateTime + span;
                setupAllTimes(dt.ToFileTimeUtc());
            }
            catch (Exception exp)
            {
                toolStripStatusLabel1.Text = STATUE.ERROR.ToString();
            }
        }
       
    }
}
