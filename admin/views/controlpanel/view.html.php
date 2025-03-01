<?php
defined('_JEXEC') or die;
class Posts2articleViewControlpanel extends JViewLegacy
{
    public function display($tpl = null)
    {
        JToolbarHelper::title('Posts2Article: Control Panel', 'puzzle');
        parent::display($tpl);
    }
}
