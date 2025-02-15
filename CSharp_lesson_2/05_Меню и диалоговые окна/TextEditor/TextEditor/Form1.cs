namespace TextEditor
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private string currentFilePath = string.Empty;


        private void btnNew_Click(object sender, EventArgs e)
        {
            if (ConfirmSaveChanges())
            {
                textBoxContent.Clear();
                currentFilePath = string.Empty;
                this.Text = "����� ���� - ��������� ��������";
            }
        }

        private void btnOpen_Click(object sender, EventArgs e)
        {
            if (ConfirmSaveChanges())
            {
                OpenFileDialog openFileDialog = new OpenFileDialog
                {
                    Filter = "��������� ����� (*.txt)|*.txt|��� ����� (*.*)|*.*",
                    Title = "������� ����"
                };

                if (openFileDialog.ShowDialog() == DialogResult.OK)
                {
                    currentFilePath = openFileDialog.FileName;
                    textBoxContent.Text = File.ReadAllText(currentFilePath);
                    this.Text = $"{Path.GetFileName(currentFilePath)} - ��������� ��������";
                }
            }
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            SaveFile();
        }

        private void btnSaveAs_Click(object sender, EventArgs e)
        {
            SaveFileAs();
        }

        private bool ConfirmSaveChanges()
        {
            if (!string.IsNullOrEmpty(textBoxContent.Text))
            {
                var result = MessageBox.Show("��������� ���������?", "��������� ��������",
                                             MessageBoxButtons.YesNoCancel, MessageBoxIcon.Question);

                if (result == DialogResult.Yes)
                {
                    return SaveFile();
                }
                else if (result == DialogResult.Cancel)
                {
                    return false;
                }
            }

            return true;
        }

        private bool SaveFile()
        {
            if (string.IsNullOrEmpty(currentFilePath))
            {
                return SaveFileAs();
            }

            File.WriteAllText(currentFilePath, textBoxContent.Text);
            MessageBox.Show("���� ������� �������.", "��������� ��������", MessageBoxButtons.OK, MessageBoxIcon.Information);
            return true;
        }

        private bool SaveFileAs()
        {
            SaveFileDialog saveFileDialog = new SaveFileDialog
            {
                Filter = "��������� ����� (*.txt)|*.txt|��� ����� (*.*)|*.*",
                Title = "��������� ���� ���"
            };

            if (saveFileDialog.ShowDialog() == DialogResult.OK)
            {
                currentFilePath = saveFileDialog.FileName;
                File.WriteAllText(currentFilePath, textBoxContent.Text);
                //this.Text = $"{Path.GetFileName(currentFilePath)} - ��������� ��������";
                MessageBox.Show("���� ������� �������.", "��������� ��������", MessageBoxButtons.OK, MessageBoxIcon.Information);
                return true;
            }

            return false;
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void textBoxContent_TextChanged(object sender, EventArgs e)
        {

        }

        private void fontToolStripMenuItem_Click(object sender, EventArgs e)
        {
            FontDialog fontDialog = new FontDialog();
            if (fontDialog.ShowDialog() == DialogResult.OK)
            {
                Font selectedFont = fontDialog.Font;
                textBoxContent.Font = selectedFont;
            }
        }

        private void backColorToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ColorDialog colorDialog = new ColorDialog();
            if (colorDialog.ShowDialog() == DialogResult.OK)
            {
                Color selectedColor = colorDialog.Color;
                textBoxContent.BackColor = selectedColor;
            }
        }
    }
}
