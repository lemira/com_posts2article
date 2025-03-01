<?php
defined('_JEXEC') or die;
require_once JPATH_COMPONENT . '/controller.php';
JLoader::register('Posts2articleController', JPATH_COMPONENT . '/controller.php');
use Joomla\CMS\Factory;
$app = Factory::getApplication();
$input = $app->input;
$controller = JControllerLegacy::getInstance('Posts2article');
$controller->execute($input->getCmd('task', 'display'));
$controller->redirect();
