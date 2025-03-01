<?php
defined('_JEXEC') or die;
class Posts2articleController extends JControllerLegacy
{
    public function display($cachable = false, $urlparams = [])
    {
        $this->input->set('view', 'params');
        parent::display($cachable, $urlparams);
    }
}
