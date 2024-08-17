controller_template_str = """
package {{ package_name }}.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import {{ package_name }}.entity.{{ entity_name }};
import {{ package_name }}.service.{{ service_name }};
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {

    @Autowired
    private SimpleService simpleService;

}

"""