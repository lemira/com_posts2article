<?php
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
