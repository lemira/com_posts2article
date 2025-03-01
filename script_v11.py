import os
import zipfile
from google.colab import files
import shutil

# Очищаем и создаём временную папку
temp_dir = 'temp_com_posts2article'
if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir)
os.makedirs(temp_dir, exist_ok=True)

# Список файлов и их содержимое (Скрипт #11)
files_content = {
    'posts2article.xml': '''<?xml version="1.0" encoding="utf-8"?>
<extension type="component" version="5.0" method="upgrade">
    <name>com_posts2article</name>
    <author>Твой Имя</author>
    <creationDate>February 2025</creationDate>
    <version>1.0.0</version>
    <description>Компонент для создания статей из тем Kunena</description>
    <files folder="site">
        <filename>index.php</filename>
        <filename>controller.php</filename>
        <folder>views</folder>
    </files>
    <administration>
        <files folder="admin">
            <filename>index.php</filename>
            <filename>controller.php</filename>
            <folder>views</folder>
        </files>
        <menu>COM_POSTS2ARTICLE</menu>
    </administration>
</extension>''',

    'admin/index.php': '''<?php
defined('_JEXEC') or die;
require_once JPATH_COMPONENT . '/controller.php';
JLoader::register('Posts2articleController', JPATH_COMPONENT . '/controller.php');
use Joomla\CMS\Factory;
$app = Factory::getApplication();
$input = $app->input;
$controller = JControllerLegacy::getInstance('Posts2article');
$controller->execute($input->getCmd('task', 'display'));
$controller->redirect();
''',

    'admin/controller.php': '''<?php
defined('_JEXEC') or die;
use Joomla\CMS\MVC\Controller\AdminController;
class Posts2articleController extends AdminController
{
    public function display($cachable = false, $urlparams = [])
    {
        $this->input->set('view', 'controlpanel');
        return parent::display($cachable, $urlparams);
    }
}
''',

    'admin/views/controlpanel/view.html.php': '''<?php
defined('_JEXEC') or die;
class Posts2articleViewControlpanel extends JViewLegacy
{
    public function display($tpl = null)
    {
        JToolbarHelper::title('Posts2Article: Control Panel', 'puzzle');
        parent::display($tpl);
    }
}
''',

    'admin/views/controlpanel/tmpl/default.php': '''<?php
defined('_JEXEC') or die;
?>
<div class="container-fluid">
    <h1>Posts2Article: Control Panel</h1>
    <p>Здесь будет работа.</p>
</div>
''',

    'site/index.php': '''<?php
defined('_JEXEC') or die;
require_once JPATH_COMPONENT . '/controller.php';
JLoader::register('Posts2articleController', JPATH_COMPONENT . '/controller.php');
use Joomla\CMS\Factory;
$app = Factory::getApplication();
$input = $app->input;
$controller = JControllerLegacy::getInstance('Posts2article');
$controller->execute($input->getCmd('task', 'display'));
$controller->redirect();
''',

    'site/controller.php': '''<?php
defined('_JEXEC') or die;
class Posts2articleController extends JControllerLegacy
{
    public function display($cachable = false, $urlparams = [])
    {
        $this->input->set('view', 'params');
        parent::display($cachable, $urlparams);
    }
}
''',

    'site/views/params/view.html.php': '''<?php
defined('_JEXEC') or die;
class Posts2articleViewParams extends JViewLegacy
{
    public function display($tpl = null)
    {
        parent::display($tpl);
    }
}
''',

    'site/views/params/tmpl/default.php': '''<?php
defined('_JEXEC') or die;
?>
<div class="container-fluid">
    <h1>Posts2Article: Параметры</h1>
    <p>Здесь будет работа.</p>
</div>
'''
}

# Создаём файлы во временной папке
for filepath, content in files_content.items():
    full_filepath = os.path.join(temp_dir, filepath)
    dir_name = os.path.dirname(full_filepath)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(full_filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip())

# Создаём ZIP
zip_path = 'com_posts2article_v11.zip'
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files in os.walk(temp_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, temp_dir)
            zipf.write(file_path, arcname)

print(f"Архив создан: {zip_path}")
if os.path.getsize(zip_path) > 0:
    print("ZIP содержит файлы и готов к скачиванию.")
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        print("Содержимое ZIP:")
        zipf.printdir()
else:
    print("Ошибка: ZIP пустой. Проверь скрипт или сессию Colab.")
print("Открой вкладку 'Files' слева, найди 'com_posts2article_v11.zip' и скачай вручную (правой кнопкой → Download).")

# Удаляем временную папку
shutil.rmtree(temp_dir)
